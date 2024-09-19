import win32api

# Call ::Beep()
win32api.Beep(500, 3000)

# Call ::GetSystemMetrics to get screen dimensions
print('Width: ', win32api.GetSystemMetrics(0))
print('Height: ', win32api.GetSystemMetrics(1))
