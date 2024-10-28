---
title: Использование Aspose.Pdf для .NET с Coldfusion
type: docs
weight: 300
url: /net/using-aspose-pdf-for-net-with-coldfusion/
description: Вы должны работать с Aspose.Pdf для .NET с Coldfusion, используя класс PdfFileInfo
lastmod: "2021-07-14"
draft: false
---

{{% alert color="primary" %}}

В этой статье мы расскажем, как использовать Aspose.PDF для .NET с Coldfusion. Это поможет вам понять детали интеграции Aspose.PDF для .Net и Coldfusion. С помощью простого примера я покажу вам процесс интеграции функциональности Aspose.PDF для .Net в ваши приложения Coldfusion.

{{% /alert %}}

## Обзор

Aspose.PDF для .NET — это компонент, который также предоставляет возможность редактировать и манипулировать существующими файлами PDF.
Aspose.PDF для .NET - это компонент, который также предоставляет возможность редактировать и управлять существующими файлами PDF.

## Предварительное условие

Для использования Aspose.PDF для .Net с Coldfusion вам потребуется IIS, .Net 2.0 и Coldfusion. Я тестировал компонент с использованием IIS 5, .Net 2.0 и Coldfusion 8. Есть еще две вещи, на которые вам нужно обратить внимание при установке Coldfusion. Во-первых, вы должны указать, какой(ие) сайт(ы) под IIS будут использовать Coldfusion. Во-вторых, вам нужно выбрать 'Службы интеграции .Net' в установщике Coldfusion. Службы интеграции .Net позволяют доступ к сборке компонентов .Net в приложениях Coldfusion; в данном случае компонентом будет Aspose.PDF для .NET.

## Объяснение

Прежде всего, вам нужно скопировать DLL (Aspose.PDF.dll) в место, откуда вы будете обращаться к нему для последующего использования; это будет установлено как путь и назначено атрибуту сборки тега cfobject, как показано ниже:

```html
<cfobject type = ".NET" name = "fileinfo" 
        class = "Aspose.PDF.Facades.PdfFileInfo" 
        assembly = "C:/Aspose/Net/Assembly/Aspose.PDF.dll">
```
Атрибут class в указанном выше теге ссылается на класс Aspose.PDF. Facades, в данном случае это PdfFileInfo. Атрибут name является именем экземпляра класса и будет использоваться позже в коде для доступа к методам или свойствам класса. Атрибут type указывает тип компонента - в нашем случае это .Net.

Одна важная деталь, о которой вам нужно помнить при использовании компонента .Net в Coldfusion, заключается в том, что при получении или установке любого свойства объекта класса, вы должны следовать определенной структуре. Для установки свойства вы будете использовать синтаксис Set_propertyname, а для получения значения свойства - Get_propertyname.

Например

Установить значение свойства:

```html
<cfset FilePath = ExpandPath("guide.pdf")>
```

Получить значение свойства:

```html
<cfoutput>#fileinfo.Get_title()#</cfoutput>
```

Простой, но полный пример, чтобы помочь вам понять процесс использования Aspose.PDF для .NET в Coldfusion, приведен ниже.

### Покажем информацию о файле PDF

```html
<!--- создаем экземпляр класса PdfFileInfo --->

<cfobject type = ".NET" name = "fileinfo" class = "Aspose.PDF.Facades.PdfFileInfo"

assembly = "C:/Aspose/Net/Assembly/Aspose.PDF.dll">

<!--- получаем путь к pdf файлу --->

<cfset FilePath = ExpandPath("guide.pdf")>

<!--- присваиваем путь к файлу pdf объекту класса, устанавливая его свойство inputfile --->

<cfset fileinfo.Set_inputfile(FilePath)>

<!--- Показываем информацию о файле --->

<cfoutput><b>Название:</b>#fileinfo.Get_title()#</cfoutput><br/>
<cfoutput><b>Тема:</b>#fileinfo.Get_subject()#</cfoutput><br/>
<cfoutput><b>Автор:</b>#fileinfo.Get_author()#</cfoutput><br/>
<cfoutput><b>Создатель:</b>#fileinfo.Get_Creator()#</cfoutput><br/>

```
## Заключение

{{% alert color="primary" %}}
В этой статье мы увидели, что, следуя некоторым основным правилам интеграции Coldfusion и .Net, мы можем добавить множество функциональных возможностей и гибкости, связанных с манипуляцией PDF документами, используя Aspose.PDF для .NET в наших приложениях Coldfusion.
{{% /alert %}}
