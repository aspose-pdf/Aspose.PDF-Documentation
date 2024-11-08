---
title: ラッパーアセンブリの作成
type: docs
weight: 80
url: /ja/net/creating-a-wrapper-assembly/
---

{{% alert color="primary" %}}

Aspose.PDF for .NET の多くのクラス、メソッド、プロパティを使用する必要がある場合は、ラッパーアセンブリを作成することを検討してください（C# または他の .NET プログラミング言語を使用）。ラッパーアセンブリは、管理されていないコードから直接 Aspose.PDF for .NET を使用することを避けるのに役立ちます。

良いアプローチは、Aspose.PDF for .NET を参照し、それを使ってすべての作業を行い、最小限のクラスとメソッドのみを管理されていないコードに公開する .NET アセンブリを開発することです。その後、アプリケーションはラッパーライブラリのみを使用するようにする必要があります。

COM Interop 経由で呼び出す必要のあるクラスとメソッドの数を減らすことで、プロジェクトが簡素化されます。.NET クラスを COM Interop 経由で使用するには、高度なスキルがしばしば必要です。

{{% /alert %}}

## Aspose.PDF for .NET ラッパー

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
            // ドキュメントを開く
            Document doc = new Document(file);

            // テキストを抽出するための TextAbsorber オブジェクトを作成
            TextAbsorber absorber = new TextAbsorber();

            // absorber をドキュメントの全ページに適用
            doc.Pages.Accept(absorber);

            // 抽出されたテキストを取得

            string text = absorber.Text;
            return text;

        }
    }
}

```

