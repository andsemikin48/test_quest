# test_reports.py
import pytest
from report_csv import generate_performance_report

def test_performance_report():
    test_data = [
        {'position': 'Developer', 'performance': '4.5'},
        {'position': 'Developer', 'performance': '4.7'},
        {'position': 'QA', 'performance': '4.3'}
    ]
    result = generate_performance_report(test_data)
    assert len(result) == 2
    assert result[0][0] == 'Developer'