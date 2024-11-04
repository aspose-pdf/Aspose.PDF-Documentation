---
title: Usando FloatingBox para geração de texto
linktitle: Usando FloatingBox
type: docs
weight: 30
url: /net/floating-box/
description: Esta página explica como formatar texto dentro de uma caixa flutuante.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

Esta funcionalidade também funciona na biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Básicos do uso da ferramenta FloatingBox

A ferramenta Floating Box é uma ferramenta especial para colocar texto e outros conteúdos em uma página PDF. Sua principal característica é o recorte de texto quando ele sobrepassa o tamanho do FloatingBox.

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

No exemplo acima, estamos criando um FloatingBox com uma largura de 400 pt e uma altura de 30 pt.
Também, neste exemplo, foi criado intencionalmente mais texto do que poderia caber no tamanho dado.
Como resultado, o texto foi cortado.

![Image 1](image01.png)

A propriedade `IsNeedRepeating` com valor `false` limita o texto a 1 página.

Se definirmos essa propriedade para `true`, o texto será refluído para a próxima página na mesma posição.

![Image 2](image02.png)

## Recursos avançados do FloatingBox

### Suporte a múltiplas colunas

#### Layout de múltiplas colunas (caso simples)

`FloatingBox` suporta layout de múltiplas colunas. Para criar tal layout, você deve definir os valores das propriedades ColumnInfo.

* `ColumnWidths` é uma string com enumeração de largura em pt.
* `ColumnSpacing` é uma string com largura do espaço entre colunas.
* `ColumnCount` é o número de colunas.

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
Nós usamos a biblioteca adicional LoremNET no exemplo acima e criamos 20 parágrafos. Esses parágrafos foram divididos em três colunas e preencheram as páginas seguintes até o texto acabar.

#### Layout de multi-colunas com início de coluna forçado

Faremos o mesmo com o exemplo seguinte como o anterior. A diferença é que criamos 3 parágrafos. Podemos forçar o FloatingBox a renderizar cada parágrafo em uma nova coluna. Para fazer isso, precisamos definir `IsFirstParagraphInColumn` quando adicionamos texto ao objeto FloatingBox.

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
### Suporte de Fundo

Você pode definir a cor de fundo desejada usando a propriedade `BackgroundColor`.

```cs
// Inicializa o objeto documento
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

### Suporte de Deslocamento

FloatingBox pode ser deslocado para outra localização configurando os valores `Top` e `Left`.

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

