# P2 方向：Lean-QuantumInfo 集成

## 现状

GitHub: [Timeroot/Lean-QuantumInfo](https://github.com/Timeroot/Lean-QuantumInfo)

### 统计 (截至 2026-05)
- **2,143 个定理**
- **423 个定义**
- **38,105 行 Lean 4 代码**
- **MIT 许可证**

### 已形式化内容
- 量子态、密度矩阵、测量
- 冯·诺依曼熵、相对熵
- 量子信道、完全正定映射
- **广义量子 Stein 引理** (2026-04 完成)
- 量子假设检验
- 资源理论框架

## 集成方案

### 1. 依赖配置 (lakefile.lean)

```lean
require quantumInfo from git
  "https://github.com/Timeroot/Lean-QuantumInfo.git"
```

### 2. DTE 使用 Lean-QuantumInfo 的定义

```lean
import QuantumInfo.Finite.Entropy
import QuantumInfo.Finite.State
import QuantumInfo.Finite.Channel

-- 使用已有的密度矩阵定义
open QuantumInfo

-- DTE G-face: 使用 QuantumInfo 的 Negativity
def DTE.G {dA dB : ℕ} (ρ : State (dA * dB)) : ℝ :=
  Negativity ρ (PartialTranspose.transpose ρ)

-- DTE I-face: 使用 QuantumInfo 的 mutualInformation  
def DTE.I {dA dB : ℕ} (ρ : State (dA * dB)) : ℝ :=
  mutualInformation ρ

-- Theorem 1: G = O 的证明可以利用已有的谱理论
```

### 3. 优先集成的定理

| Lean-QuantumInfo 模块 | DTE 应用 | 状态 |
|----------------------|---------|------|
| `State.lean` | 密度矩阵结构 | ✅ 可直接用 |
| `Entropy.lean` | von Neumann 熵 S(ρ) | ✅ 可直接用 |
| `Channel.lean` | CPTP 映射、Partial Trace | ✅ 可直接用 |
| `SteinsLemma.lean` | 资源理论 | 🔄 可映射到 DTE 分类 |
| `Distance.lean` | 保真度、迹距离 | 🔄 可定义 DTE-Bures |

### 4. 立即行动项

1. **fork Lean-QuantumInfo** 为子模块
2. **重写 DTE/Core.lean** 使用 `QuantumInfo.State`
3. **证明 Theorem 1**: `G = O` 利用已有的谱分解定理
4. **证明 Theorem 2**: `I ≥ cG²` 利用 `Entropy` 中的不等式

### 5. MerLean 自动形式化

论文: [MerLean: An Agentic Framework For Autoformalization in Quantum Computation](https://arxiv.org/abs/2602.16554)

**架构**:
```
LaTeX 论文
  ↓ Statement Extraction (LLM)
JSON 数学声明
  ↓ Iterative Formalization (compile-fix loop)
Lean 4 代码
  ↓ Faithfulness Checking
验证后的形式化
```

**应用到 DTE**:
1. 将 `DTE_Paper_Framework.md` 输入 MerLean
2. 自动生成 Lean 4 代码
3. 人工审核并补全 `sorry`
4. 提交到 Mathlib 或独立库

## 时间线

| 周 | 任务 |
|----|------|
| 1 | Fork Lean-QuantumInfo，配置 lake 依赖 |
| 2 | 重写 Core.lean，使用 QuantumInfo API |
| 3 | 完成 Theorem 1 证明 |
| 4 | 完成 Theorem 2 证明 (d=2) |
| 5 | 完成 Theorem 3 证明 |
| 6-8 | MerLean 自动形式化其余定理 |
