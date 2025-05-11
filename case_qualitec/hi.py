from dash import Dash, html
from dash_bootstrap_components.themes import BOOTSTRAP
from components.layout import create_layout
from plots.data import data_ploting

def main() -> None:
    weeks = ["Semana_1","Semana_2","Semana_3"]
    key_index_1 = [19, 25, 35]
    key_index_2 = [20, 15, 12]
    key_index_3 = [90.14, 75, 82]
    key_index_4 = [60, 73, 57]

    df = data_ploting(weeks=weeks, index=key_index_1)
    print

    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "KPI's Dashboard"
    app.layout = create_layout(app)
    app.run()

if __name__ == "__main__":
    main()