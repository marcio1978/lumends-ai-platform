"""
LAP Core State

Responsável pelo estado de execução do agente.
"""

from pydantic import BaseModel


class AgentState(BaseModel):
    """
    Estado durante uma execução do LAP.
    """

    message: str
    response: str | None = None
