[English](Home) · **Dansk** · [Bahasa Melayu](Home-ms)

# Miles to Kilometer Converter

Et lille Tkinter-program, der omregner miles til kilometer: skriv en afstand, tryk på Calculate og læs resultatet.

![Konverteren efter omregning af 10 miles](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-mile2km-converter/raw/branch/main/docs/images/converter-result.png)


## Hvad er det?

Dag 27 af Udemy-kurset *100 Days of Code: The Complete Python Pro Bootcamp*. Vinduet har et indtastningsfelt til afstanden i miles, en etiket, der viser resultatet i kilometer, og en knap, **Calculate**. Omregningsreglen er holdt adskilt fra vinduet, så den kan testes uden en skærm. Faktoren 1,609 og alle vinduets tekster er konstanter i `constants.py`. Tekst, der ikke er et tal, viser "Enter a number" i stedet for et resultat.

## Hvad øvelsen lærer dig

- At bygge et vindue med Tkinter: `Tk`, `Entry`, `Label` og `Button`
- At placere elementerne i et gitter med `grid`
- At køre en funktion, når der trykkes på en knap, med argumentet `command`
- At læse teksten i et indtastningsfelt med `get` og vise et resultat ved at ændre en etiket med `config`
- At gøre tekst til et tal og håndtere tekst, der ikke er et tal
- At holde omregningsreglen fri af vinduet, så den kan testes uden en skærm

## Hvad det gør

- Et indtastningsfelt til afstanden i miles og en knap, **Calculate**
- Resultatet i kilometer, afrundet til to decimaler, med faktoren 1,609
- Beskeden "Enter a number", når teksten ikke er et tal
- Tests af omregningen, der altid kører, og tests af vinduet, der kører, når Tkinter og en skærm er tilgængelige
- Ingen afhængigheder ved kørsel ud over Pythons standardbibliotek

## Videre

- [Kom godt i gang](Getting-Started-da)
- [Projektdokumenter](Project-Documents-da)
