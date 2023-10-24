import json
from flask import Flask, render_template, jsonify
from flask import request


from data_services.InfoscoutDataService import get_basket_id_trend_data, get_table_counts_data, get_daily_counts_trend_data, get_source_tables_counts_data, get_count_of_baskets_data
from data_services.AirflowDataService import get_panel_airflow_DAG_runs_data, get_rde_airflow_DAG_runs_data


app = Flask(__name__)


@app.route('/side_nav')
def side_nav():
    return render_template('side_nav.html')  


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/panel_airflow_dags')
def panel_airflow_dags():
    return render_template('panel_airflow_dags.html')


@app.route('/rde_airflow_dags')
def rde_airflow_dags():
    return render_template('rde_airflow_dags.html')


@app.route('/source_tables_stats')
def source_tables_stats():
    return render_template('source_tables_stats.html')


@app.route('/get_panel_airflow_DAG_runs', methods=['GET', 'POST'])
def get_panel_airflow_DAG_runs():
    data = get_panel_airflow_DAG_runs_data()
    return {'data': data}


@app.route('/get_rde_airflow_DAG_runs', methods=['GET', 'POST'])
def get_rde_airflow_DAG_runs():
    data = get_rde_airflow_DAG_runs_data()
    return {'data': data}


@app.route('/get_table_counts', methods=['GET', 'POST'])
def get_table_counts():
    data = get_table_counts_data()
    return {'data': data}


@app.route('/get_source_tables_counts', methods=['GET', 'POST'])
def get_source_tables_counts():
    data = get_source_tables_counts_data()
    return {'data': data}


@app.route('/get_basket_id_trend', methods=['GET', 'POST'])
def get_basket_id_trend():
    json_data = json.loads(request.get_data().decode("utf-8"))
    table_name = json_data['table_name']

    data = get_basket_id_trend_data(table_name)
    data = {
        table_name : data
    }

    return {'data': data}


@app.route('/get_daily_counts_trend', methods=['GET', 'POST'])
def get_daily_counts_trend():
    f_basket_denorm = get_daily_counts_trend_data('F_BASKET_DENORM')
    f_basket_item_denorm = get_daily_counts_trend_data('F_BASKET_ITEM_DENORM')
    d_item = get_daily_counts_trend_data('D_ITEM')

    data = {
        'F_BASKET_DENORM': f_basket_denorm,
        'F_BASKET_ITEM_DENORM': f_basket_item_denorm,
        'D_ITEM': d_item
    }

    return {'data': data}


@app.route('/get_count_of_baskets', methods=['GET', 'POST'])
def get_count_of_baskets():
    counts = get_count_of_baskets_data()
    return {'data': counts}



if __name__ == "__main__":
    app.run(debug=False, port=5000, host="0.0.0.0")
