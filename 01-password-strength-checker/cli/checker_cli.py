from unittest import result
from rich.console import Console
from rich.panel import Panel
from password_checker import overall_strength

console= Console()

def main():
    password=input("Enter your password: ")
    result = overall_strength(password)

    if result=="Weak":
        colored="[bold red]Weak[/bold red]"
    elif result=="Medium":
        colored="[bold yellow]Medium[/bold yellow]"
    else:
        colored="[bold green]Strong[/bold green]"
    console.print(Panel(f"Password Strength: {colored}", expand=False))

if __name__=="__main__":
    main()