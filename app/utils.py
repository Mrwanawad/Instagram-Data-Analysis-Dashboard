def human_readable(n):
    if n >= 1_000_000_000:
        return f"{n/1_000_000_000:.0f}Bn"
    elif n >= 1_000_000:
        return f"{n/1_000_000:.0f}Mn"
    elif n >= 1_000:
        return f"{n/1_000:.0f}K"
    else:
        return str(n)
    
instagram_palette = [
    "#1F6AE1",  # Blue
    "#3A5BDC",  # Blue-Purple
    "#5A4FD6",  # Indigo
    "#7A3FCB",  # Purple
    "#9B3CB4",  # Violet
    "#C13584",  # Magenta
    "#E1306C",  # Pink
    "#F56040",  # Orange
    "#FCAF45",  # Light Orange
    "#FFD166"   # Yellow
]    