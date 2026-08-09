"""
DTE Visualization Module
=======================

3D fingerprint plots, evolution graphs, and entanglement landscape visualizations.
"""

import numpy as np
from typing import Optional, List, Tuple
import logging

from .core import DTETriple, EntanglementType

logger = logging.getLogger("dte.viz")


class DTEVisualizer:
    """
    Visualization tools for DTE analysis.
    
    Requires matplotlib. Install with: pip install dte-core[viz]
    """
    
    def __init__(self, style: str = "default"):
        self.style = style
        try:
            import matplotlib
            matplotlib.use("Agg")  # Non-interactive backend
            import matplotlib.pyplot as plt
            self.plt = plt
            self._available = True
        except ImportError:
            self._available = False
            logger.warning("matplotlib not available. Install with: pip install matplotlib")
    
    def fingerprint_3d(self, triples: List[DTETriple],
                       labels: Optional[List[str]] = None,
                       title: str = "DTE 3D Fingerprint",
                       save_path: Optional[str] = None) -> Optional[object]:
        """
        Plot DTE triples in 3D (G, I, O) space.
        
        Args:
            triples: List of DTETriple objects
            labels: Optional labels for each point
            title: Plot title
            save_path: Path to save figure
            
        Returns:
            matplotlib Figure or None if matplotlib unavailable
        """
        if not self._available:
            return None
        
        from mpl_toolkits.mplot3d import Axes3D
        
        fig = self.plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        colors = self._get_colors(triples)
        
        xs = [t.G for t in triples]
        ys = [t.I for t in triples]
        zs = [t.O for t in triples]
        
        scatter = ax.scatter(xs, ys, zs, c=colors, s=100, alpha=0.8, edgecolors='black')
        
        ax.set_xlabel('G (Geometric / Negativity)', fontsize=12)
        ax.set_ylabel('I (Information / Mutual Info)', fontsize=12)
        ax.set_zlabel('O (Open / Boundary)', fontsize=12)
        ax.set_title(title, fontsize=14, fontweight='bold')
        
        # Add legend for classification colors
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='green', label='Separable'),
            Patch(facecolor='orange', label='PPT-Bound'),
            Patch(facecolor='red', label='NPT')
        ]
        ax.legend(handles=legend_elements, loc='upper left')
        
        if save_path:
            fig.savefig(save_path, dpi=150, bbox_inches='tight')
            logger.info(f"Saved 3D fingerprint to {save_path}")
        
        return fig
    
    def evolution_plot(self, times: List[float],
                       triples: List[DTETriple],
                       save_path: Optional[str] = None) -> Optional[object]:
        """
        Plot DTE triple evolution over time.
        
        Args:
            times: Time points
            triples: DTE triples at each time point
            save_path: Path to save figure
        """
        if not self._available:
            return None
        
        fig, axes = self.plt.subplots(3, 1, figsize=(10, 10), sharex=True)
        
        labels = ['G (Geometric)', 'I (Information)', 'O (Open)']
        values = [[t.G for t in triples], [t.I for t in triples], [t.O for t in triples]]
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
        
        for ax, label, vals, color in zip(axes, labels, values, colors):
            ax.plot(times, vals, color=color, linewidth=2, marker='o', markersize=4)
            ax.set_ylabel(label, fontsize=11)
            ax.grid(True, alpha=0.3)
            ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
        
        axes[-1].set_xlabel('Time', fontsize=12)
        axes[0].set_title('DTE Triple Evolution', fontsize=14, fontweight='bold')
        
        self.plt.tight_layout()
        
        if save_path:
            fig.savefig(save_path, dpi=150, bbox_inches='tight')
        
        return fig
    
    def werner_phase_diagram(self, d: int = 2,
                             save_path: Optional[str] = None) -> Optional[object]:
        """
        Plot Werner state phase diagram (p vs DTE values).
        
        Args:
            d: Dimension
            save_path: Path to save figure
        """
        if not self._available:
            return None
        
        from .core import DTECoreEngine
        from .states import StateGenerator
        
        ps = np.linspace(0, 1, 101)
        Gs, Is, Os = [], [], []
        
        engine = DTECoreEngine(d, d)
        gen = StateGenerator()
        
        for p in ps:
            rho = gen.werner_state(p, d)
            t = engine.triple(rho)
            Gs.append(t.G)
            Is.append(t.I)
            Os.append(t.O)
        
        fig, ax = self.plt.subplots(figsize=(10, 6))
        ax.plot(ps, Gs, label='G (Geometric)', linewidth=2)
        ax.plot(ps, Is, label='I (Information)', linewidth=2)
        ax.plot(ps, Os, label='O (Open)', linewidth=2, linestyle='--')
        
        ax.axvline(x=1/(d+1), color='gray', linestyle=':', label=f'PPT threshold p={1/(d+1):.3f}')
        ax.set_xlabel('p (Werner parameter)', fontsize=12)
        ax.set_ylabel('DTE value', fontsize=12)
        ax.set_title(f'Werner State Phase Diagram (d={d})', fontsize=14, fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        if save_path:
            fig.savefig(save_path, dpi=150, bbox_inches='tight')
        
        return fig
    
    def _get_colors(self, triples: List[DTETriple]) -> List[str]:
        """Map classification to colors."""
        color_map = {
            EntanglementType.SEPARABLE: '#2ecc71',   # green
            EntanglementType.PPT_BOUND: '#f39c12',   # orange
            EntanglementType.NPT: '#e74c3c',         # red
            EntanglementType.UNKNOWN: '#95a5a6',     # gray
        }
        return [color_map[t.classify()] for t in triples]


def generate_all_figures(output_dir: str = ".") -> List[str]:
    """
    Generate all standard DTE figures.
    
    Returns:
        List of saved figure paths
    """
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    viz = DTEVisualizer()
    from .states import StateGenerator
    from .core import DTECoreEngine
    
    paths = []
    
    # 1. 3D fingerprint
    gen = StateGenerator()
    triples = []
    for p in np.linspace(0, 1, 11):
        engine = DTECoreEngine(2, 2)
        triples.append(engine.triple(gen.werner_state(p, 2)))
    
    path = f"{output_dir}/dte_fingerprint_3d.png"
    viz.fingerprint_3d(triples, title="Werner State DTE Fingerprint", save_path=path)
    paths.append(path)
    
    # 2. Werner phase diagram
    path = f"{output_dir}/werner_phase_diagram.png"
    viz.werner_phase_diagram(d=2, save_path=path)
    paths.append(path)
    
    logger.info(f"Generated {len(paths)} figures in {output_dir}")
    return paths
