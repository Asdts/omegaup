class AgentError(Exception):
    """Base class for all agent-related errors."""


class AgentNotFoundError(AgentError):
    """Raised when an agent is not found."""

    def __init__(self, agent_name: str):
        super().__init__(f"Agent '{agent_name}' not found.")
        self.agent_name = agent_name

class LLMMaxRetryError(Exception):
    """Raised when the maximum number of retries for an LLM call is reached."""

    def __init__(self, calls_retried: int,llm_backend: str = None):
        self.calls_retried = calls_retried
        self.llm_backend = llm_backend
        self.message = f"Max retries reached for {llm_backend} after {calls_retried} attempts."
        super().__init__(self.message)
        