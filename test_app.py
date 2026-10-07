from app import calculate_deployment_time

# testet, ob die Funktion aus app korrekt funktioniert
def test_calculate_deployment_time():
    result = calculate_deployment_time(4, 1)
    assert result["manual_days"] == 4
    assert result["automated_hours"] == 1
    assert "faster" in result["improvement"]
