```
---
title: Стрелки на Линиях
type: docs
weight: 20
url: /reportingservices/line-arrows/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Спецификация RDL не определяет стрелки для элемента линии, поэтому конструктор отчетов не поддерживает установку стрелок для линий. С Aspose.Pdf для Reporting Services вы можете сделать это легко.

{{% /alert %}}

{{% alert color="primary" %}}

В настоящее время рендерер Aspose.PDF поддерживает добавление стрелок в начале или в конце линий путем добавления пользовательских свойств.

Добавить стрелку в начале линии  
**Имя пользовательского свойства**: HasArrowAtStart  
**Значение пользовательского свойства**: True  

Добавить стрелку в конце линии  
**Имя пользовательского свойства**: HasArrowAtEnd  
**Значение пользовательского свойства**: True  

Например, в текущем файле отчета есть две линии с именами 'line1' и 'line2', и у line1 есть стрелка в начале, а у line2 - стрелки в начале и в конце. Для удовлетворения этих требований вы можете добавить пользовательские свойства, как в следующем фрагменте кода.

**Пример**

{{< highlight csharp >}}

 <Line Name="line1">
```

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
```