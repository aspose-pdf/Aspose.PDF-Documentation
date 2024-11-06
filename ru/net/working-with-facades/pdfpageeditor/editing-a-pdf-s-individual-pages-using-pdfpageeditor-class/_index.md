---
title: Редактирование отдельных страниц PDF
type: docs
weight: 20
url: ru/net/editing-a-pdf-s-individual-pages-using-pdfpageeditor-class/
description: В этом разделе объясняется, как редактировать отдельные страницы PDF с помощью класса PdfPageEditor.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Пространство имен Aspose.Pdf.Facades в [Aspose.PDF для .NET](/pdf/net/) позволяет управлять отдельными страницами в PDF файле. Эта функция помогает работать с отображением страниц, выравниванием и переходами и т.д. Класс PdfPageEditor помогает достичь этой функциональности. В этой статье мы рассмотрим свойства и методы, предоставляемые этим классом, а также работу этих методов.

{{% /alert %}}

## Объяснение

Класс [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) отличается от классов [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) и [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). Сначала нам нужно понять разницу, а затем мы сможем лучше понять класс PdfPageEditor. Класс PdfFileEditor позволяет вам управлять всеми страницами в файле, такими как добавление, удаление или объединение страниц и т. д., в то время как класс PdfContentEditor помогает вам управлять содержимым страницы, т.е. текстом и другими объектами и т. д. Тогда как класс PdfPageEditor работает только с самой отдельной страницей, например, вращение, масштабирование и выравнивание страницы и т. д.

Мы можем разделить функции, предоставляемые этим классом, на три основные категории, т.е. Переход, Выравнивание и Отображение. Мы собираемся обсудить эти категории ниже:

### Переход

Этот класс содержит два свойства, связанные с переходом, т.е. 
[TransitionType](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/transitiontype) и [TransitionDuration](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/transitionduration). TransitionType указывает стиль перехода, который будет использоваться при переходе на эту страницу с другой страницы во время презентации. TransitionDuration указывает продолжительность отображения для страниц.

### Alignment

Класс PdfPageEditor поддерживает как горизонтальное, так и вертикальное выравнивание.
``` Он предоставляет два свойства для достижения цели, а именно [Alignment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/alignment) и [VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/VerticalAlignment). Свойство Alignment используется для выравнивания содержимого по горизонтали. Свойство Alignment принимает значение AlignmentType, которое содержит три варианта: Center, Left и Right. Свойство VerticalAlignment принимает значение VerticalAlignmentType, которое содержит три варианта: Bottom, Center и Top.

### Display

В категорию отображения мы можем включить такие свойства, как PageSize, Rotation, Zoom и DisplayDuration. PageSize свойство указывает размер отдельной страницы в файле. Это свойство принимает объект PageSize в качестве входных данных, который включает в себя предопределенные размеры страниц, такие как A0, A1, A2, A3, A4, A5, A6, B5, Letter, Ledger и P11x17. Свойство Rotation используется для установки вращения отдельной страницы. Оно может принимать значения 0, 90, 180 или 270. Свойство Zoom устанавливает коэффициент увеличения для страницы и принимает значение типа float в качестве входных данных. Этот класс также предоставляет метод для получения размера страницы и вращения страницы отдельной страницы в файле.

Вы можете найти примеры вышеупомянутых методов в приведенном ниже фрагменте кода:



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-EditPdfPages-EditPdfPages.cs" >}}

## Заключение

{{% alert color="primary" %}}
В этой статье мы более подробно рассмотрели класс [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor). We have elaborated the properties and methods provided by this class. It makes the manipulation of individual pages in a class a very easy and simple task.  
Мы подробно описали свойства и методы, предоставляемые этим классом. Это делает манипуляцию отдельными страницами в классе очень легкой и простой задачей.  
{{% /alert %}}