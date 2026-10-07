# zeigt rechnerisch, wie viel schneller CI/CD gegenüber dem manuellen Prozess bei StreamDesk ist
def calculate_deployment_time(manual_days, automated_hours): # Funktion nimmt zwei Werte entgegen
    return {
        "manual_days": manual_days,
        "automated_hours": automated_hours,
        "improvement": f"{manual_days * 24 / automated_hours:.1f}x faster" # rechnet Tage in Stunden um
    }

if __name__ == "__main__":
    result = calculate_deployment_time(4, 1)
    print(f"Improvement: {result['improvement']}")
