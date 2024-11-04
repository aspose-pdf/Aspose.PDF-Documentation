---
title: 래퍼 어셈블리 생성
type: docs
weight: 80
url: /net/creating-a-wrapper-assembly/
---

{{% alert color="primary" %}}

Aspose.PDF for .NET의 많은 클래스, 메소드 및 속성을 사용해야 하는 경우 래퍼 어셈블리를 생성하는 것을 고려해 보세요( C# 또는 다른 .NET 프로그래밍 언어를 사용). 래퍼 어셈블리는 비관리 코드에서 직접 Aspose.PDF for .NET을 사용하는 것을 피하는 데 도움이 됩니다.

좋은 접근 방식은 Aspose.PDF for .NET을 참조하는 .NET 어셈블리를 개발하고 그것과 모든 작업을 처리하며, 비관리 코드에는 최소한의 클래스와 메소드만 노출하는 것입니다. 그러면 귀하의 응용 프로그램은 귀하의 래퍼 라이브러리만을 사용하여 작업해야 합니다.

COM Interop을 통해 호출해야 하는 클래스와 메소드의 수를 줄이면 프로젝트가 간소화됩니다. .NET 클래스를 COM Interop을 통해 사용하는 것은 종종 고급 기술을 필요로 합니다.

{{% /alert %}}

## Aspose.PDF for .NET 래퍼

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
            // 문서 열기
            Document doc = new Document(file);

            // 텍스트 추출을 위한 TextAbsorber 객체 생성
            TextAbsorber absorber = new TextAbsorber();

            // 모든 문서 페이지에 대해 absorber 적용
            doc.Pages.Accept(absorber);

            // 추출된 텍스트 가져오기

            string text = absorber.Text;
            return text;

        }
    }
}

```

