---
title: Instalando a Licença Aspose.Pdf para SharePoint
type: docs
weight: 10
url: /sharepoint/installing-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: Depois de estar satisfeito com sua avaliação, você pode adquirir uma licença para o PDF SharePoint API e seguir as instruções de instalação para aplicá-la. 
---

{{% alert color="primary" %}}

Depois de estar satisfeito com sua avaliação, você pode [adquirir uma licença](https://purchase.aspose.com/buy). Antes de adquirir, certifique-se de entender e concordar com os termos de assinatura da licença.

{{% /alert %}}

{{% alert color="primary" %}}

A licença será enviada por e-mail após o pagamento do pedido. A licença é um arquivo .zip contendo um pacote regular de solução SharePoint.

Este arquivo contém:

- Aspose.PDF.SharePoint.License.wsp

Arquivo de pacote de solução SharePoint. A Licença Aspose.PDF para SharePoint é empacotada como uma solução SharePoint para facilitar a implantação/remoção em toda a fazenda de servidores.

- readme.txt

Instruções de instalação da licença.
 Instalação da licença é realizada a partir do console do servidor via stsadm.exe. Os passos necessários para instalar a licença são fornecidos abaixo.

**Nota:** Os caminhos são omitidos para clareza. Você pode precisar adicionar o caminho real para o stsadm.exe e/ou o arquivo de solução ao executá-los.

1. Execute stsadm para adicionar a solução ao repositório de soluções do SharePoint:

stsadm.exe -o addsolution -filename Aspose.PDF.SharePoint.License.wsp

2. Implante a solução em todos os servidores na farm:

stsadm.exe -o deploysolution -name Aspose.PDF.SharePoint.License.wsp -immediate -force

3. Execute trabalhos administrativos de temporização para completar a implantação imediatamente.

stsadm.exe -o execadmsvcjobs

**Nota:** Você receberá um aviso ao executar o passo de implantação se o serviço de Administração do Windows SharePoint Services não estiver iniciado. Stsadm.exe depende deste serviço e do Windows SharePoint Timer Service para replicar dados da solução através da farm. Se estes serviços não estiverem em execução na sua farm de servidores, você pode precisar implantar a licença em cada servidor.