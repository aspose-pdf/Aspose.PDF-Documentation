---
title: Visual Studio Export GridView To PDF Control
type: docs
weight: 10
url: ru/net/visual-studio-export-gridview-to-pdf-control/
---

## Введение

Export GridView To Pdf Control - это серверный контрол ASP.NET, который позволяет экспортировать содержимое GridView в документ Pdf с использованием [Aspose.PDF](http://www.aspose.com/.net/pdf-component.aspx). Он добавляет кнопку **Экспорт в Pdf** в верхней части контрола GridView. Нажатие на кнопку динамически экспортирует содержимое контрола GridView в документ Pdf, а затем автоматически загружает экспортированный файл на место на диске, выбранное пользователем, всего за пару секунд.

### Особенности модуля

Эта начальная версия контрола предоставляет следующие функции:

- Получите офлайн-копию вашего любимого онлайн-содержимого GridView для редактирования, обмена и печати в очень популярном документе Pdf.
- Наследуется от стандартного контрола ASP.NET GridView, следовательно, имеет все его функции и свойства.
- Работает со всеми версиями .NET, начиная с .NET 2.0.
- Возможность настройки/локализации текста кнопки Экспорта.
- Возможность настройки/локализации текста кнопки "Экспорт".
- Опция экспорта в альбомном режиме, если содержимое GridView шире и не помещается в стандартном портретном режиме.
- Применение внешнего вида вашей собственной темы на кнопку "Экспорт" с использованием CSS.
- Возможность добавления пользовательского заголовка в верхней части экспортируемого документа.
- Возможность сохранения каждого экспортируемого документа на сервере по настраиваемому пути на диске.
- Возможность экспорта текущей страницы или всех страниц, когда включена пагинация.

## Системные требования и поддерживаемые платформы

### Системные требования

Контроль экспорта GridView в PDF для Visual Studio может быть использован на любой системе, где установлены IIS и .NET framework версии 2.0 или выше.

### Поддерживаемые платформы

Контроль экспорта GridView в PDF для Visual Studio поддерживается всеми версиями ASP.NET, работающими на .NET framework версии 2.0 или выше. Вы можете использовать любую из следующих версий Visual Studio для использования этого контроля в ваших приложениях ASP.NET:

- Visual Studio 2005
- Visual Studio 2008
- Visual Studio 2010
- Visual Studio 2012
- Visual Studio 2013

## Скачивание
## Скачивание

Вы можете скачать Export GridView To Pdf Control из одного из следующих мест

- [CodePlex](https://asposevs.codeplex.com/releases/view/617022)
- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/releases/tag/AsposeExportGridViewToPdfControl_1.0)

## Установка

Установка Export GridView To Pdf Control очень проста и легка, пожалуйста, следуйте этим простым шагам

### **Для Visual Studio 2010, 2012 и 2013**

1. Распакуйте скачанный zip-файл, например, Aspose.PDF.GridViewExport_1.0.zip
1. Дважды щелкните файл VSIX Aspose.PDF.GridViewExport.vsix
1. Появится диалоговое окно, показывающее доступные и поддерживаемые версии Visual Studio, установленные на вашем компьютере
1. Выберите те, к которым вы хотите добавить Export GridView To Pdf Control.
1. Нажмите Установить

После завершения установки появится диалоговое окно об успешном завершении.

**Примечание:** Пожалуйста, убедитесь, что вы перезапустили Visual Studio для вступления изменений в силу.

### **Для Visual Studio 2005, 2008 и Express editions**

Пожалуйста, следуйте этим шагам для интеграции Export GridView To Pdf Control в Visual Studio для удобного перетаскивания, как и другие элементы управления ASP.NET
Пожалуйста, следуйте этим шагам для интеграции контроля экспорта GridView в PDF в Visual Studio для удобного перетаскивания, как и другие элементы управления ASP.NET

1. Извлеките скачанный zip-файл, т.е. Aspose.PDF.GridViewExport.NET2.0_1.0.zip
1. Убедитесь, что запускаете Visual Studio от имени администратора

В меню Инструменты выберите Пункты Панели Инструментов.

1. Нажмите Обзор.
   Откроется диалоговое окно Открыть.
1. Перейдите в извлеченную папку и выберите Aspose.PDF.GridViewExport.dll
1. Нажмите ОК.

Когда вы откроете элемент управления aspx или ascx в левой части Панели инструментов, вы увидите ExportGridViewToPdf на вкладке Общие

![todo:image_alt_text](visual-studio-export-gridview-to-pdf-control_2.png)

## Использование

После установки начать использовать этот контроль в ваших приложениях ASP.NET очень просто

|**Для .NET framework 4.0 и выше**|**Для .NET framework 2.0 и выше**|** |
| :- | :- | :- |
|Для приложений, работающих на .NET framework 4.0 и выше в Visual Studio 2010 и выше, вы должны увидеть элемент управления **ExportGridViewToPdf** на вкладке **Aspose** на панели инструментов, как показано ниже.
|Для приложений, работающих на платформе .NET framework версии 4.0 и выше в Visual Studio 2010 и выше, вы должны увидеть элемент управления **ExportGridViewToPdf** на вкладке **Aspose** на панели инструментов, как показано ниже.

### Ручное добавление элемента управления ExportGridViewToPdf

Если у вас возникли проблемы с использованием вышеуказанных методов, которые используют панель инструментов Visual Studio, вы можете вручную добавить этот элемент управления в ваше ASP.NET приложение, работающее на любой версии .NET framework выше 2.0

1. Если вы используете Visual Studio, убедитесь, что запускаете её от имени администратора
1. Добавьте ссылку на **Aspose.PDF.GridViewExport.dll**, доступный в распакованном загруженном пакете в вашем ASP.NET проекте или веб-приложении. Убедитесь, что ваше веб-приложение/Visual Studio имеет полный доступ к этой папке, иначе вы можете получить исключение Отказано в доступе.
1. Добавьте эту строку в верхнюю часть страницы, элемента управления или MasterPage

```csharp
 <%@ Register assembly="Aspose.PDF.GridViewExport" namespace="Aspose.PDF.GridViewExport" tagprefix="aspose" %>
```
```csharp
<aspose:ExportGridViewToPdf ID="ExportGridViewToPdf1" runat="server"></aspose:ExportGridViewToPdf>
```

### Часто задаваемые вопросы

Распространенные вопросы и проблемы, с которыми вы можете столкнуться при использовании этого элемента управления

<div class="schema-faq-code" itemscope="" itemtype="https://schema.org/FAQPage">
    <div itemscope="" itemprop="mainEntity" itemtype="https://schema.org/Question" class="faq-question">
        <h3 itemprop="name" class="faq-q">1. Не вижу элемент управления ExportGridViewToPdf в панели инструментов</h3>
        <div itemscope="" itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
             <div itemprop="text" class="faq-a">
               <p><strong>Visual Studio 2010 и выше</strong></p>
<ol><li>Убедитесь, что вы установили этот элемент управления с помощью файла расширения VSIX, найденного в загруженном пакете. Чтобы проверить, перейдите в Инструменты -&gt; Расширения и обновления. В разделе Установленные вы должны увидеть 'Aspose Export Export GridView To Pdf Control'. Если вы не видите его, попробуйте переустановить его</li>
<li>Убедитесь, что ваше веб-приложение работает на .NET framework 4.0 или выше, для более низких версий .NET framework, пожалуйста, проверьте вышеуказанный альтернативный метод.

<li>Убедитесь, что ваше веб-приложение работает на платформе .NET версии 4.0 или выше, для более ранних версий платформы .NET смотрите альтернативный метод выше.
Старые версии Visual Studio</li>
<li>Убедитесь, что вы вручную добавили этот элемент в вашу панель инструментов согласно предыдущим инструкциям.</li></ol>
        </div>
    </div>
</div>

<div itemscope="" itemprop="mainEntity" itemtype="https://schema.org/Question" class="faq-question">
    <h3 itemprop="name" class="faq-q">2. При запуске приложения возникает ошибка 'Доступ запрещен'</h3>
    <div itemscope="" itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
        <div itemprop="text" class="faq-a">
            <ol>
            <li>Если у вас возникает эта проблема в продакшене, убедитесь, что вы скопировали оба файла Aspose.PDF.dll и Aspose.PDF.GridViewExport.dll в вашу папку bin.</li>
            <li>Если вы используете Visual Studio, убедитесь, что запускаете её от имени администратора, даже если вы уже вошли как администратор.</li>

<li>Если вы используете Visual Studio, убедитесь, что запускаете её от имени администратора, даже если вы уже вошли в систему как администратор.</li>
</ol>
</div>
</div>
</div>
</div>

### **Свойства контроля экспорта Aspose .NET Export GridView в PDF**

Ниже приведены свойства для настройки и использования крутых функций этого контроля

|**Название свойства**|**Тип**|**Пример/Возможные значения**|**Описание**|
| :- | :- | :- | :- |
|ExportButtonText|string|Экспорт в PDF|Вы можете использовать это свойство для переопределения существующего текста по умолчанию|
|ExportButtonCssClass|string|btn btn-primary|Css класс, который применяется к внешнему div кнопки экспорта. Для применения css к кнопке вы можете использовать .yourClass input|
|ExportInLandscape|bool|true or false|Если true, изменяет ориентацию выходного документа на альбомную. По умолчанию - портретная|
| | | | |
|ExportFileHeading|string|Пример отчета по экспорту GridView|Вы можете использовать html теги для добавления стиля к вашему заголовку|
|ExportOutputPathOnServer|string|c:/temp|Локальный путь на сервере, где автоматически сохраняется копия экспорта|
```
|ExportOutputPathOnServer|string|c:/temp|Локальный путь на сервере, где автоматически сохраняется копия экспорта.
|ExportDataSource|object|allRowsDataTable|Устанавливает объект, из которого этот элемент управления привязкой данных извлекает свой список элементов данных. Объект должен содержать все данные, которые необходимо экспортировать. Это свойство используется в дополнение к обычному свойству DataSource и полезно, когда включена пользовательская разбивка на страницы и текущая страница извлекает только строки, которые должны быть отображены на экране.
|LicenseFilePath|string| |Локальный путь на сервере к файлу лицензии. Например, c:/inetpub/Aspose.PDF.lic|

Пример элемента управления "Экспорт GridView в Pdf" со всеми используемыми свойствами показан ниже

```csharp
<aspose:ExportGridViewToPdf Width="800px" ID="ExportGridViewToPdf1" ExportButtonText="Экспортировать в Pdf"
    CssClass="table table-hover table-bordered" ExportButtonCssClass="myClass" ExportOutputFormat="Doc"
    ExportInLandscape="true" ExportOutputPathOnServer="c:\\temp" ExportFileHeading="<h4>Пример отчета</h4>"
    OnPageIndexChanging="ExportGridViewToPdf1_PageIndexChanging" PageSize="5" AllowPaging="True"
    LicenseFilePath="c:\\inetpub\\Aspose.PDF.lic"
    runat="server" CellPadding="4" ForeColor="#333333" GridLines="Both">
</aspose:ExportGridViewToPdf>
```
## Видео демонстрация

Пожалуйста, посмотрите [видео](https://www.youtube.com/watch?v=WNJ7T8u4JlM) ниже, чтобы увидеть модуль в действии.

### Поддержка

С самых первых дней Aspose мы знали, что просто предоставление нашим клиентам хороших продуктов будет недостаточно. Нам также нужно было обеспечить хорошее обслуживание. Мы сами являемся разработчиками и понимаем, как разочаровывает, когда техническая проблема или особенность программного обеспечения мешает вам делать то, что вам нужно. Мы здесь, чтобы решать проблемы, а не создавать их.

Именно поэтому мы предлагаем бесплатную поддержку. Каждый, кто использует наш продукт, независимо от того, купил ли он его или использует оценочную версию, заслуживает нашего полного внимания и уважения.

Вы можете сообщить о любых проблемах или предложениях, связанных с этим Pdf, используя любую из следующих платформ

- [CodePlex](https://asposevs.codeplex.com/workitem/list/basic)
- [Visual Studio Gallery - Q and A](https://visualstudiogallery.msdn.microsoft.com/fb8b9944-cfe5-44a9-8aa7-c785d32d1066)
- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/issues)
- [Microsoft Developer Network - Q and A](https://code.msdn.microsoft.com/Aspose-NET-Export-GridView-caddbb6d/view/Discussions#content)
- [Сеть разработчиков Microsoft - Вопросы и ответы](https://code.msdn.microsoft.com/Aspose-NET-Export-GridView-caddbb6d/view/Discussions#content)

### Расширение и участие

Aspose .NET Export GridView в Pdf для Visual Studio является открытым проектом, и его исходный код доступен на крупнейших социальных платформах программирования, перечисленных ниже. Разработчики могут скачать исходный код и расширить функциональность в соответствии со своими требованиями.

#### Исходный код

Вы можете получить последнюю версию исходного кода с одного из следующих мест

- [CodePlex](https://asposevs.codeplex.com/SourceControl/latest#Aspose.PDF.GridViewExport/)
- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/tree/master/Plugins/Visual%20Studio/Aspose.PDF.GridViewExport)

#### Как настроить исходный код

Для работы с исходным кодом необходимо установить следующее

- Visual Studio 2010

Пожалуйста, следуйте этим простым шагам, чтобы начать

1. Скачайте/Клонируйте исходный код.
1.
1.
1. Перейдите к последнему скачанному исходному коду и откройте **Aspose.PDF.GridViewExport.sln**

#### Обзор исходного кода

В решении три проекта

- Aspose.PDF.GridViewExport - Содержит пакет VSIX и серверный Pdf для .NET 4.0.
- Aspose.PDF.GridViewExport_DotNet_2.0 - Расширенный GridView Pdf для .NET 2.0
- Aspose.PDF.GridViewExport.Website - Веб-проект для тестирования экспортируемого в Word GridView Pdf
