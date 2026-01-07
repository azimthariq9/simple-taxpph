def hitung_pph_tahunan(netto_bulanan: int, status: str) -> float:
    ptkp =54000000  # PTKP untuk status TK/0
    pkp = max(0, (netto_bulanan * 12) - ptkp)
    return pkp * 0.5