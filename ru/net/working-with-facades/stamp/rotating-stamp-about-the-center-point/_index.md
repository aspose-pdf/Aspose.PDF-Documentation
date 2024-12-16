---
title: Вращение штампа вокруг центральной точки
type: docs
weight: 10
url: /ru/net/rotating-stamp-about-the-center-point/
description: Этот раздел объясняет, как вращать штамп вокруг центральной точки с использованием класса Stamp.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

[Пространство имен Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) в [Aspose.PDF для .NET](/pdf/ru/net/) позволяет добавлять штамп в существующий PDF-файл. Иногда пользователям необходимо вращать штамп. В этой статье мы рассмотрим, как вращать штамп вокруг его центральной точки.

{{% /alert %}}

## Детали реализации

Класс [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) позволяет добавлять водяной знак в PDF-файл. Вы можете указать изображение, которое будет добавлено в качестве штампа, используя метод [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.stamp/bindimage/methods/1). Метод [SetOrigin](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setorigin) позволяет установить начало координат добавленного штампа; это начало координат — нижние левые координаты штампа. Вы также можете установить размер изображения, используя метод [SetImageSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setimagesize).

Теперь мы видим, как штамп может быть повернут вокруг центра штампа. [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) класс предоставляет свойство с именем Rotation. Это свойство устанавливает или получает вращение содержимого штампа от 0 до 360. Мы можем указать любое значение вращения от 0 до 360. Указав значение вращения, мы можем повернуть штамп вокруг его центральной точки. Если Stamp является объектом типа Stamp, то значение вращения можно указать как aStamp.Rotation = 90. В этом случае штамп будет повернут на 90 градусов вокруг центра содержимого штампа. Следующий фрагмент кода показывает, как повернуть штамп вокруг центральной точки: 

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-RotatingStamp-RotatingStamp.cs" >}}