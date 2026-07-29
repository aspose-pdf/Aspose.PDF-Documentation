---
title: Стрелки линии
linktitle: Стрелки линии
type: docs
weight: 20
url: /ru/reportingservices/line-arrows/
description: Узнайте, как добавить стрелки к линиям в PDF‑отчетах с помощью Aspose.PDF for Reporting Services. Легко улучшайте визуальное оформление отчетов.
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Спецификация RDL не определяет стрелки для элемента line, поэтому Report Builder не поддерживает настройку стрелок для линии. С помощью Aspose.PDF for Reporting Services вы можете легко сделать это.

{{% /alert %}}

{{% alert color="primary" %}}

В настоящее время рендерер Aspose.PDF поддерживает добавление стрелок в начале или в конце линий с помощью пользовательских свойств.

Добавить стрелку в начале линии  
**Свойство** **Имя**: HasArrowAtStart  
**Значение свойства**: True  

Добавить стрелку в конце линии  
**Свойство** **Имя**: HasArrowAtEnd  
**Значение свойства**: True  

Например, в текущем файле отчёта есть две линии с именами 'line1' и 'line2', при этом line1 имеет стрелку в начале, line2 — стрелку в начале и в конце; чтобы удовлетворить этим требованиям, вы можете добавить пользовательские свойства, как показано в следующем фрагменте кода.

**Пример**

{{< highlight csharp >}}
 <Line Name="line1">
    <Style>
      ......
    </style>
    <CustomProperties>
      <CustomProperty>
        <Name>HasArrowAtStart</Name>
        <Value>Истина</Value>
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
        <Value>Истина</Value>
      </CustomProperty>
<CustomProperty>
        <Name>ИмеетСтрелкуВКонце</Name>
        <Value>Истина</Value>
      </CustomProperty>
    </CustomProperties>
</Line>

{{< /highlight >}}
{{% /alert %}}
