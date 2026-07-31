"""
LAP Engine

Controlador principal do agente.
"""

from app.core.burr.workflow import create_workflow


class LAPEngine:

    def process(self, message: str):

        workflow = create_workflow(message)

        result = workflow.run(
            halt_after=[
                "generate_response"
            ]
        )

        # O Burr retorna uma tupla contendo:
        # (última ação, resultado, estado)

        state = result[2]

        return {
            "message": state["message"],
            "response": state["response"]
        }
