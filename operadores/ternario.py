lockdown = False
grana = 600

status = "Em casa" if lockdown or grana <= 100 else 'Uhuuu'

print(f'{status}')