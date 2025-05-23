"""BrahminyKite Framework Package - Unified philosophical verification and consensus.

Organized verification frameworks:
- empirical: Fact-checking, academic sources, statistical validation
- contextual: NLP, cultural analysis, situational relevance  
- consistency: Formal logic, theorem proving, contradiction detection
- power_dynamics: Bias detection, perspective diversity, stakeholder analysis
- utility: Cost-benefit analysis, actionability, outcome simulation
- evolution: Temporal robustness, learning, adaptation
- llm_integration: LLM + formal verification synergy

Core types and consensus mechanisms also available.
"""

from .consensus_types import (
    VerificationMode,
    ConsensusProposal,
    ProposalType,
    NodeContext,
    PaxosMessage,
    ConsensusVerificationResult
)

from .legacy.frameworks import (
    Claim,
    VerificationResult
)

# Import verification frameworks
from .empirical import RealEmpiricalFramework
from .contextual import RealContextualFramework  
from .consistency import RealConsistencyFramework, FormalConsistencyFramework
from .power_dynamics import RealPowerDynamicsFramework
from .utility import RealUtilityFramework
from .llm_integration import LLMFormalIntegration

__all__ = [
    # Core types
    "VerificationMode",
    "Claim", 
    "ConsensusProposal",
    "ProposalType",
    "NodeContext",
    "PaxosMessage",
    "VerificationResult",
    "ConsensusVerificationResult",
    
    # Verification frameworks
    "RealEmpiricalFramework",
    "RealContextualFramework",
    "RealConsistencyFramework", 
    "FormalConsistencyFramework",
    "RealPowerDynamicsFramework",
    "RealUtilityFramework",
    "LLMFormalIntegration"
]