"""
LAP Engine

Ponto central de execução dos agentes.
"""

from app.core.state import AgentState
from app.core.workflow import LAPWorkflow


class LAPEngine:

    def __init__(self):
        self.workflow = LAPWorkflow()

    def process(self, message: str) -> AgentState:
        """
        Entrada principal do LAP.
        """

        state = AgentState(
            message=message
        )

        return self.workflow.execute(state)
