def read_rows(lines: list[str]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    headers: list[str] | None = None

    for line in lines:
        if not line.strip():
            continue

        fields = [field.strip() for field in line.split(',')]
        if headers is None:
            headers = fields
            continue
        if len(fields) != len(headers):
            continue

        rows.append(dict(zip(headers, fields)))

    return rows

def count_types(rows: list[dict[str, str]]) -> dict[str, int]:
    counts: dict[str, int] = {}

    for row in rows:
        kind = row.get('тип')
        if kind is not None:
            counts[kind] = counts.get('тип', 0) + 1

    return counts

def total_minutes(rows: list[dict[str, str]], kind: str) -> float:
    total = 0.0

    for row in rows:
        if row.get('тип') != kind:
            continue
        total += float(row.get('минуты', '').replace(',', '.'))

    return round(total, 1)

def to_csv(counts: dict[str, int]) -> str:
    lines = ['тип, количество']    

    for kind in sorted(counts):
        lines.append(f'{kind},{counts[kind]}')

    return '\n'.join(lines) + '\n'