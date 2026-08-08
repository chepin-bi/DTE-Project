# P2 方向：神经科学应用 — DTE 分析 fMRI/EEG 数据

## 理论基础

### Integrated Information Theory (IIT) 与 DTE 的对应

| IIT 概念 | DTE 对应 | 关系 |
|---------|---------|------|
| Φ (integrated information) | I(A:B) | I 面直接量化整合信息 |
| Cause-effect structure | G = Ext¹ | 几何面编码因果结构 |
| Exclusion principle | O = Σ\|λ₋\| | 开面保证唯一性 |

### DTE 神经科学假设

> **Neuro-DTE Hypothesis**: 大脑功能网络在任何时刻的状态可以用 DTE 三重 (G, I, O) 刻画，其中：
> - I ∝ Φ：整合信息与互信息成正比
> - G ∝ 因果连接强度：几何面反映有效连接
> - O ∝ 模块化程度：开面反映网络分离度

## 数据管道设计

```
fMRI/EEG 原始数据
    ↓
预处理 (SPM/MNE-Python)
    ↓
功能连接矩阵 C(t) —— 皮尔逊相关 / 格兰杰因果
    ↓
密度矩阵 ρ(t) = C(t) / Tr(C(t))  [需正定化]
    ↓
DTECoreEngine(d_a, d_b).triple(ρ(t))
    ↓
时间序列: G(t), I(t), O(t)
    ↓
分析: 意识状态分类 / 疾病检测 / 脑机接口
```

## Python 实现

```python
import numpy as np
from dte_core import DTECoreEngine

class DTENeuroAnalyzer:
    """DTE analysis for neuroimaging data."""
    
    def __init__(self, n_rois):
        # 假设 ROI 分为左右半球
        self.engine = DTECoreEngine(n_rois//2, n_rois//2)
    
    def connectivity_to_density(self, corr_matrix):
        """Convert correlation matrix to density matrix."""
        # 谱截断保证正定性
        evals, evecs = np.linalg.eigh(corr_matrix)
        evals = np.maximum(evals, 1e-10)
        evals = evals / np.sum(evals)
        rho = evecs @ np.diag(evals) @ evecs.T
        return rho
    
    def analyze_timeseries(self, corr_timeseries):
        """Analyze time series of connectivity matrices."""
        results = []
        for C in corr_timeseries:
            rho = self.connectivity_to_density(C)
            triple = self.engine.triple(rho)
            results.append(triple.to_dict())
        return results
    
    def consciousness_index(self, triple):
        """Quantify consciousness level."""
        # I 面主导意识水平
        return triple.I / (1 + triple.G + triple.O)
```

## 预期应用

| 应用领域 | DTE 指标 | 预期发现 |
|---------|---------|---------|
| 麻醉深度监测 | I(t) 动态 | I → 0 表示意识丧失 |
| 睡眠分期 | G(t), I(t) 模式 | REM 期 I 峰值 |
| 精神分裂症 | O(t) 异常 | 模块化丧失 → O 升高 |
| 阿尔茨海默病 | G(t) 下降 | 长程连接退化 |
| 脑机接口 | 实时 I(t) | 意识意图编码 |

## 数据集

- **OpenNeuro**: https://openneuro.org
- **Human Connectome Project (HCP)**: https://www.humanconnectome.org
- **EEGMIDB**: PhysioNet EEG Motor Movement/Imagery Dataset

## 开放问题

| # | 问题 | 优先级 |
|---|------|--------|
| NS-1 | 功能连接矩阵正定化的最佳方法 | P0 |
| NS-2 | DTE 三重与 IIT-Φ 的定量校准 | P0 |
| NS-3 | 时序 DTE 的动态系统模型 | P1 |
| NS-4 | 多被试统计检验框架 | P1 |
| NS-5 | 实时 EEG DTE 解码器 | P2 |
