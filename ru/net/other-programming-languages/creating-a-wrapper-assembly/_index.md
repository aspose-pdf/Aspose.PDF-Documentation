---
title: Создание Сборки-Оболочки
type: docs
weight: 80
url: /ru/net/creating-a-wrapper-assembly/
---

{{% alert color="primary" %}}

Если вам необходимо использовать множество классов, методов и свойств Aspose.PDF для .NET, рассмотрите возможность создания сборки-оболочки (используя C# или любой другой язык программирования .NET). Сборки-оболочки помогают избежать прямого использования Aspose.PDF для .NET из неуправляемого кода.

Хороший подход заключается в разработке сборки .NET, которая ссылается на Aspose.PDF для .NET и выполняет всю работу с ним, а также предоставляет неуправляемому коду только минимальный набор классов и методов. Ваше приложение должно затем работать только с вашей библиотекой-оболочкой.

Уменьшение количества классов и методов, которые вам нужно вызывать через COM Interop, упрощает проект. Использование классов .NET через COM Interop часто требует продвинутых навыков.

{{% /alert %}}

## Оболочка Aspose.PDF для .NET

```csharp

using System;
using System.Runtime.InteropServices;
namespace PdfText
{
    [Guid("FC969AC9-6591-46FB-A4AB-DB12A776F3BF")]
    [InterfaceType(ComInterfaceType.InterfaceIsIDispatch)]
    public interface IPetriever
    {
        [DispId(1)]
        void SetLicense(string file);

        [DispId(2)]
        string GetText(string file);
    }

    [Guid("3D59100F-3CC5-463D-B509-58FA0520B436")]
    [ClassInterface(ClassInterfaceType.None)]

    [ComSourceInterfaces(typeof(IPetriever))]

    public class Petriever : IPetriever
    {
        public void SetLicense(string file)
        {
            License lic = new License();
            lic.SetLicense(file);
        }

        public string GetText(string file)
        {
            // открыть документ
            Document doc = new Document(file);

            // создать объект TextAbsorber для извлечения текста
            TextAbsorber absorber = new TextAbsorber();

            // принять absorber для всех страниц документа
            doc.Pages.Accept(absorber);

            // получить извлеченный текст

            string text = absorber.Text;
            return text;

        }
    }
}

```

