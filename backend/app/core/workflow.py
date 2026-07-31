"""
LAP Workflow

Primeiro fluxo de processamento.
"""

from app.core.state import AgentState


class LAPWorkflow:

    def execute(self, state: AgentState) -> AgentState:
        """
        Executa o workflow atual.
        """

        state.response = (
            f"Mensagem recebida pelo LAP: {state.message}"
        )

        return state
