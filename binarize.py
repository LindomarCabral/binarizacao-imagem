import cv2
import numpy as np

# FUNÇÃO PRÓPRIA para converter colorido para tons de cinza
def rgb_para_cinza(imagem_colorida):
    altura, largura, canais = imagem_colorida.shape
    imagem_cinza = np.zeros((altura, largura), dtype=np.uint8)
    
    for i in range(altura):
        for j in range(largura):
            # Fórmula padrão para conversão RGB → Cinza
            r = imagem_colorida[i, j, 2]  # Canal Vermelho
            g = imagem_colorida[i, j, 1]  # Canal Verde  
            b = imagem_colorida[i, j, 0]  # Canal Azul
            cinza = 0.299 * r + 0.587 * g + 0.114 * b
            imagem_cinza[i, j] = int(cinza)
    
    return imagem_cinza

# FUNÇÃO PRÓPRIA para binarização
def binarizar_imagem(imagem, limiar=60):
    altura, largura = imagem.shape
    imagem_binaria = np.zeros((altura, largura), dtype=np.uint8)
    
    for i in range(altura):
        for j in range(largura):
            if imagem[i, j] >= limiar:
                imagem_binaria[i, j] = 255  # Branco
            else:
                imagem_binaria[i, j] = 0    # Preto
    
    return imagem_binaria

# CARREGA A IMAGEM
img_colorida = cv2.imread('jaguar.png')
if img_colorida is None:
    print("Erro ao carregar imagem!")
    exit()

# CONVERSÃO USANDO NOSSAS FUNÇÕES
print("Convertendo colorido → tons de cinza...")
img_cinza = rgb_para_cinza(img_colorida)

print("Binarizando com limiar 60...")
img_binaria = binarizar_imagem(img_cinza, limiar=60)

# EXIBE APENAS AS TRÊS IMAGENS PRINCIPAIS
cv2.imshow("1 - Imagem Original Colorida", img_colorida)
cv2.imshow("2 - Imagem em Tons de Cinza", img_cinza)
cv2.imshow("3 - Imagem Binarizada (Preto e Branco)", img_binaria)

print("\nPressione qualquer tecla para fechar as janelas...")
cv2.waitKey(0)
cv2.destroyAllWindows()

# SALVA RESULTADOS
cv2.imwrite('jaguar_cinza.jpg', img_cinza)
cv2.imwrite('jaguar_binaria.jpg', img_binaria)

print("\nProcessamento concluído!")
print("✓ Conversão colorido → tons de cinza: FEITA com nossa função")
print("✓ Binarização cinza → preto/branco: FEITA com nossa função") 
print("✓ Limiar utilizado: 60")
print("✓ Imagens salvas: jaguar_cinza.jpg, jaguar_binaria.jpg")
print("\nAtende ao desafio: TODAS as conversões foram feitas com funções próprias!")