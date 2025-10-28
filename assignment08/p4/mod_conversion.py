
def in2cm_table_html(start: float, end: float, step: float) -> str:
    html=""""
    <html>
    <header>
        <title> Inches to centimeter conversion </title>
    </header>
    <body>
        <table border="1" cellpadding="5">
            <tr>
                <th> inch</th>
                <th> cm </th>
            <tr>
    """
    length = start
    while length <= end:
        cm = length * 2.54
        html+=f"<tr><td>{length:.1f}</td><td>{cm:.1f} </td> </tr>"
        length += step
    html += "</table>\n</body>\n</html>"
    return html

