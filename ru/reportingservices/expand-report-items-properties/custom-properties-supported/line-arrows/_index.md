---
title: Линейные стрелки
linktitle: Линейные стрелки
type: docs
weight: 20
url: /reportingservices/line-arrows/
description: Научитесь добавлять стрелки в отчеты PDF с помощью Aspose.PDF для Reporting Services. Улучшайте визуальные эффекты отчета без особых усилий.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Спецификация RDL не определяет стрелки для элемента линии, поэтому построитель отчетов не поддерживает настройку стрелок для линии. С помощью Aspose.PDF for Reporting Services вы можете сделать это легко.

{{% /alert %}}

В настоящее время средство рендеринга Aspose.PDF поддерживает добавление стрелок в начале или конце линий путем добавления пользовательских свойств.

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

Например, есть две строки с именем `line1` и `line2` в текущем файле отчета, а строка 1 имеет стрелку начала, строка 2 имеет стрелки начала и конца. Чтобы удовлетворить этим требованиям, вы можете добавить пользовательские свойства, как в следующем фрагменте кода.

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

