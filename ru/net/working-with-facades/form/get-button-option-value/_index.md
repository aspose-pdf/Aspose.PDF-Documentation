---
title: Получить Значение Опции Кнопки
type: docs
weight: 40
url: /ru/net/get-button-option-value/
description: Этот раздел объясняет, как получить значение опции кнопки с использованием Aspose.PDF Facades и класса Form.
lastmod: "2021-06-05"
draft: false
---

## Получение Значений Опций Кнопок из Существующего PDF Файла

Радиокнопки предоставляют способ показать различные опции. Класс [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) позволяет получить все значения опций кнопок для конкретной радиокнопки. Вы можете получить эти значения с помощью метода [GetButtonOptionValues](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptionvalues). Этот метод требует имя радиокнопки в качестве входного параметра и возвращает Hashtable. Вы можете перебрать этот Hashtable, чтобы получить значения опций. Следующий фрагмент кода показывает, как получить значения опций кнопок из существующего PDF файла.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-GetButtonOptionValue-GetButtonOptionValue.cs" >}}

## Получить текущее значение опции кнопки из существующего PDF файла

Радиокнопки предоставляют способ установки значений опций, однако в один момент может быть выбрана только одна из них. Если вы хотите получить текущее выбранное значение опции, то вы можете использовать метод [GetButtonOptionCurrentValue**. Класс [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) предоставляет этот метод. Метод [GetButtonOptionCurrentValue](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptioncurrentvalue) требует имя радиокнопки в качестве входного параметра и возвращает значение в виде строки. Следующий фрагмент кода показывает, как получить текущее значение опции кнопки из существующего PDF файла.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-GetButtonOptionValue-GetCurrentValue.cs" >}}