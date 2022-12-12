from dataclasses import dataclass
from datetime import date

@dataclass
class ItemSpecificatie:

    ordernummer: str
    itemnummer: int
    pdf: str
    aantal_per_rol: int
    aantal_rollen: int
    rolwikkeling_id: int
    rolwikkeling: str
    kernid: int
    duedate: date
    klantnaam: int
    vormid: int
    vorm: str
    cuttingdie: str
    labelwidth: float
    labelheight: float

    kolommen: list

def lead_in():
    ...

def rolwikkelingen():
    ...


