---
title: Стрелки линии
linktitle: Стрелки линии
type: docs
weight: 20
url: /ru/reportingservices/line-arrows/
description: Узнайте, как добавить стрелки к линиям в PDF‑отчётах с помощью Aspose.PDF for Reporting Services. Улучшайте визуальное оформление отчётов без усилий.
lastmod: "2026-08-20"
---

{{% alert color="primary" %}}

Спецификация RDL не определяет стрелки для элемента линии, поэтому Report Builder не поддерживает настройку стрелок для линии. С помощью Aspose.PDF for Reporting Services вы можете легко сделать это.

{{% /alert %}}

В настоящее время рендерер Aspose.PDF поддерживает добавление стрелок в начале или в конце линий посредством добавления пользовательских свойств.

```text
Add Start Arrow for Line  
Custom Property `Name`: HasArrowAtStart  
Custom Property `Value`: True  
```

```text
Add End Arrow for Line  
Custom Property `Name`: HasArrowAtEnd  
Custom Property `Value`: True  
```

Например, есть две строки, названные `line1` и `line2` в текущем файле отчета, и line1 имеет стрелку в начале, line2 имеет стрелки в начале и в конце, чтобы удовлетворить этим требованиям, вы можете добавить пользовательские свойства, как в следующем фрагменте кода.

## Пример

```xml
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
```


