---
title: Usando FloatingBox para la generación de texto
linktitle: Usando FloatingBox
type: docs
weight: 30
url: es/net/floating-box/
description: Esta página explica cómo formatear texto dentro de un cuadro flotante.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

Esta característica también funciona en la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Conceptos básicos sobre el uso de la herramienta FloatingBox

La herramienta Floating Box es una herramienta especial para colocar texto y otros contenidos en una página PDF. Su característica principal es el recorte de texto cuando se superpone al tamaño del FloatingBox.

```cs
Document document = new Document();
Page page = document.Pages.Add();
var box = new FloatingBox(400, 30)
{
    Border = new BorderInfo(BorderSide.All, 1.5f, Color.DarkGreen),
    IsNeedRepeating = false,
};
var text = LoremNET.Lorem.Paragraph(20, 6);
box.Paragraphs.Add(new TextFragment(text));
page.Paragraphs.Add(box);
```  

En el ejemplo anterior, estamos creando un FloatingBox con un ancho de 400 pt y una altura de 30 pt.
Además, en este ejemplo, se creó intencionalmente más texto del que podría caber en el tamaño dado.
Como resultado, el texto fue cortado.

![Image 1](image01.png)

La propiedad `IsNeedRepeating` con valor `false` limita el texto a 1 página.

Si configuramos esta propiedad en `true`, el texto fluirá a la siguiente página en la misma posición.

![Image 2](image02.png)

## Funciones avanzadas de FloatingBox

### Soporte multi-columna

#### Diseño de múltiples columnas (caso simple)

`FloatingBox` soporta un diseño de múltiples columnas. Para crear tal diseño, debes definir los valores de las propiedades de ColumnInfo.

* `ColumnWidths` es una cadena con enumeración de ancho en pt.
* `ColumnSpacing` es una cadena con el ancho del espacio entre columnas.
* `ColumnCount` es un número de columnas.

```cs
Document document = new Document();
Page page = document.Pages.Add();
page.PageInfo.Margin = new MarginInfo(36, 18, 36, 18);
var columnCount = 3;
var spacing = 10;
var width = page.PageInfo.Width 
    - page.PageInfo.Margin.Left 
    - page.PageInfo.Margin.Right 
    - (columnCount - 1) * spacing;
var columnWidth = width / 3;
var box = new FloatingBox()
{
    IsNeedRepeating = true
};
box.ColumnInfo.ColumnWidths = $"{columnWidth} {columnWidth} {columnWidth}";
box.ColumnInfo.ColumnSpacing = "{spacing}";
box.ColumnInfo.ColumnCount = columnCount;
var paragraphs = LoremNET.Lorem.Paragraphs(20, 8, 20);
foreach (var paragraph in paragraphs)
{
    box.Paragraphs.Add(new TextFragment(paragraph));
}

page.Paragraphs.Add(box);

document.Save("sample.pdf");
```
Usamos la librería adicional LoremNET en el ejemplo anterior y creamos 20 párrafos. Estos párrafos se dividieron en tres columnas y llenaron las páginas siguientes hasta que se agotó el texto.

#### Diseño de varias columnas con inicio de columna forzado

Haremos lo mismo con el siguiente ejemplo como en el anterior. La diferencia es que creamos 3 párrafos. Podemos forzar a FloatingBox a renderizar cada párrafo en una nueva columna. Para hacer eso, necesitamos establecer `IsFirstParagraphInColumn` cuando agregamos texto al objeto FloatingBox.

```cs
Document document = new Document();
Page page = document.Pages.Add();
page.PageInfo.Margin = new MarginInfo(36, 18, 36, 18);
var columnCount = 3;
var spacing = 10;
var width = page.PageInfo.Width 
    - page.PageInfo.Margin.Left 
    - page.PageInfo.Margin.Right 
    - (columnCount - 1) * spacing;
var columnWidth = width / 3;
var box = new FloatingBox()
{
    IsNeedRepeating = true
};
box.ColumnInfo.ColumnWidths = $"{columnWidth} {columnWidth} {columnWidth}";
box.ColumnInfo.ColumnSpacing = "{spacing}";
box.ColumnInfo.ColumnCount = 3;

var paragraphs = LoremNET.Lorem.Paragraphs(20, 8, 3);
foreach (var paragraph in paragraphs)
{
    var text = new TextFragment(paragraph)
    {
        IsFirstParagraphInColumn = true
    };
    box.Paragraphs.Add(text);
}

page.Paragraphs.Add(box);

document.Save("sample.pdf");
```
### Soporte de fondo

Puedes establecer el color de fondo deseado utilizando la propiedad `BackgroundColor`.

```cs
// Inicializar el objeto documento
Document document = new Document();
Page page = document.Pages.Add();
var box = new FloatingBox(400, 60)
{
    IsNeedRepeating = false,
    BackgroundColor = Color.LightGreen,
};
var text = LoremNET.Lorem.Paragraph(20, 6);
box.Paragraphs.Add(new TextFragment(text));
page.Paragraphs.Add(box);
```

### Soporte de desplazamiento

FloatingBox puede ser desplazado a otra ubicación estableciendo los valores `Top` y `Left`.

```cs
Document document = new Document();
Page page = document.Pages.Add();

var box = new FloatingBox()
{
    Top = -45,
    Left = 15,
    Border = new BorderInfo(BorderSide.All, 1.5f, Color.DarkGreen)
};
var text = LoremNET.Lorem.Paragraph(20, 6);
box.Paragraphs.Add(new TextFragment(text));

page.Paragraphs.Add(new TextFragment(LoremNET.Lorem.Paragraph(20, 6)));
page.Paragraphs.Add(box);            
page.Paragraphs.Add(new TextFragment(LoremNET.Lorem.Paragraph(20, 6)));
```

