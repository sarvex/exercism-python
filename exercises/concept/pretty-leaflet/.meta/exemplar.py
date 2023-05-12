import calendar
from typing import List, Optional


def capitalize_header(event_name: str) -> str:
    return event_name.capitalize()

def format_date(event_date: List[int]) -> str:
    date, month, year = event_date
    month_name = calendar.month_name[month]

    # pylint: disable=consider-using-f-string
    return f'{month_name} {date}, {year}'

def display_icons(icons: List[str]) -> List[str]:
    return [f'{icon}' for icon in icons]

def print_leaflet(event_name: str, icons: List[str], authors: List[str], event_date: Optional[List[int]]=None):
    row_full = ''.join(['*'] * 20)
    empty_row = f'*{"":^18}*'
    event_name = capitalize_header(event_name)
    icons = display_icons(icons)
    date_string = format_date(event_date) if event_date is not None else ''

    poster = [
        row_full,
        empty_row,
        f'*{event_name!r:^18}*',
        empty_row,
        f'*{date_string!s:^18}*',
        empty_row,
    ]
    for position, _ in enumerate(authors):
        icon = icons[position] if position < len(icons) else '    '
        poster.append(f'*{"":>1}{authors[position]:<11}{icon:>3}{"":>2}*')
    poster.extend((empty_row, row_full))
    return '\n'.join(poster)
