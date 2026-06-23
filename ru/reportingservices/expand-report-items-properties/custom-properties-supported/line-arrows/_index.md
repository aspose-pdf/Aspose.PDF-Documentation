---
title: Стрелки линии
linktitle: Стрелки линии
type: docs
weight: 20
url: /ru/reportingservices/line-arrows/
description: Узнайте, как добавлять стрелки к линиям в PDF‑отчетах с помощью Aspose.PDF for Reporting Services. Улучшайте визуальное оформление отчётов без усилий.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Спецификация RDL не определяет стрелки для элемента line, поэтому Report Builder не поддерживает настройку стрелок для линий. С помощью Aspose.Pdf for Reporting Services вы можете легко это сделать.

{{% /alert %}}

{{% alert color="primary" %}}

В настоящее время рендерер Aspose.PDF поддерживает добавление стрелок в начале или в конце линий с помощью пользовательских свойств.

Добавить начальную стрелку к линии  
**Пользовательское свойство** **Имя**: HasArrowAtStart  
**Значение пользовательского свойства**: True  

Добавить конечную стрелку к линии  
**Пользовательское свойство** **Имя**: HasArrowAtEnd  
**Значение пользовательского свойства**: True  

Например, в текущем файле отчета есть две линии с именами 'line1' и 'line2', при этом line1 имеет начальную стрелку, line2 имеет начальную и конечную стрелки; чтобы удовлетворить этим требованиям, вы можете добавить пользовательские свойства, как показано в следующем фрагменте кода.

**Пример**

{{< highlight csharp >}}
 <Line Name="line1">
    <Style>
      ......
    </style>
    <CustomProperties>
      <CustomProperty>
        <Name>HasArrowAtStart</Name>
        <Value>True</Value>
      </CustomProperty>
    </CustomProperties>
</Line>
......
<Line Name="line2">
    <Style>
      ......
    </style>
    <CustomProperties>
      <CustomProperty>
        <Name>HasArrowAtStart</Name>
        <Value>True</Value>
      </CustomProperty>
<CustomProperty>
        <Name>HasArrowAtEnd</Name>
        <Value>True</Value>
      </CustomProperty>
    </CustomProperties>
</Line>

{{< /highlight >}}
{{% /alert %}}

