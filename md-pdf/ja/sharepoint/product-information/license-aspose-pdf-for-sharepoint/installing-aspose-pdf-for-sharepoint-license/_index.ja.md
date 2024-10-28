---

title: Aspose.Pdf for SharePoint ライセンスのインストール

type: docs

weight: 10

url: /sharepoint/installing-aspose-pdf-for-sharepoint-license/

lastmod: "2020-12-16"

description: 評価に満足したら、PDF SharePoint API のライセンスを購入し、インストール手順に従って適用します。

---

{{% alert color="primary" %}}

評価に満足したら、[ライセンスを購入](https://purchase.aspose.com/buy)できます。購入前に、ライセンスのサブスクリプション条件を理解し、同意することを確認してください。

{{% /alert %}}

{{% alert color="primary" %}}

注文が支払われた後、ライセンスはメールで送信されます。ライセンスは、通常の SharePoint ソリューション パッケージを含む .zip アーカイブです。

このアーカイブには以下が含まれています:

- Aspose.PDF.SharePoint.License.wsp

SharePoint ソリューション パッケージ ファイル。Aspose.PDF for SharePoint ライセンスは、サーバーファーム全体での展開/撤回を容易にするために、SharePoint ソリューションとしてパッケージ化されています。

- readme.txt

ライセンスのインストール手順。


 ライセンスのインストールは、サーバーコンソールからstsadm.exeを使用して行われます。ライセンスをインストールするために必要な手順は以下の通りです。

**注:** 明確にするためにパスは省略されています。実行時にstsadm.exeやソリューションファイルへの実際のパスを追加する必要があるかもしれません。

1. stsadmを実行して、ソリューションをSharePointソリューションストアに追加します。

stsadm.exe -o addsolution -filename Aspose.PDF.SharePoint.License.wsp

2. ソリューションをファーム内のすべてのサーバーに展開します。

stsadm.exe -o deploysolution -name Aspose.PDF.SharePoint.License.wsp -immediate -force

3. 管理タイマージョブを実行して、展開を即座に完了させます。

stsadm.exe -o execadmsvcjobs

**注:** Windows SharePoint Services Administrationサービスが開始されていない場合、展開ステップを実行すると警告を受けることがあります。Stsadm.exeはこのサービスとWindows SharePoint Timer Serviceに依存しており、ソリューションデータをファーム全体に複製します。これらのサービスがサーバーファームで実行されていない場合、各サーバーでライセンスを展開する必要があるかもしれません。