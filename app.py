from flask import Flask, request, render_template, Response
from calcul import make_operation
from database import persist_operation, get_all_csv

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    operation = request.args.get('result')

    value = ""
    error_message = ""
    info = True

    if operation:
        info = False
        try:
            value = make_operation(operation)

            if value == int(value):
                value = str(int(value))
            else:
                value = str(value)

            persist_operation(operation=operation, result=value)

        except Exception as e:
            value = operation
            error_message = f"{e}"
            persist_operation(operation=operation, result=f"Error : {error_message}")

    return render_template("index.html", value=value, error_message=error_message, info=info)


@app.route("/downloadCSV")
def download_csv():
    csv = get_all_csv()
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                     "attachment; filename=operation_data.csv"})


if __name__ == '__main__':
    app.run()
