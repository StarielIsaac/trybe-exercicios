from typing import Dict, List


def total_sales_by_console(games_data: List[Dict]) -> Dict:
    result = dict()
    for game in games_data:
        console = game["Release"]["Console"]
        sales = game["Metrics"]["Sales"]
        # print(console, sales)

        if console in result:
            result[console] += sales
        else:
            result[console] = sales
    return result