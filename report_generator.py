import datetime

def generate_report(results, output_path):
    with open(output_path, 'w') as f:
        f.write("<html><head><title>SusDroid Report</title></head><body>")
        f.write(f"<h2>SusDroid Analysis Report - {datetime.datetime.now()}</h2><hr>")
        for file, matches in results.items():
            f.write(f"<h4>{file}</h4><ul>")
            for match in matches:
                f.write(f"<li><b>{match}</b></li>")
            f.write("</ul>")
        f.write("</body></html>")