#include <stdio.h>

float sd = 0;
float sq;
float dp;
char opcao[2];



int main() {
    system("clear");
    printf("\nBem vindo ao Banco XYZ\n\n");

    printf("1 - Para Saldo\n");
    printf("2 - Para Saque\n");
    printf("3 - Para Depósito\n");
    printf("4 - Para Sair\n");
    printf("\nDigite a opção desejada: ");

    while(opcao != -0){
        scanf("%s", &opcao[2]);
        switch (opcao[2]) {
            case '1':
                printf("Seu Saldo é R$ %.2f\n\n", sd);
                printf("\nPara voltar ao menu anterior, digite 9! \n");
                break;

            case '2':
                printf("Digite o Valor para saque: R$ \n");
                if(scanf("%f", &sq) != 1){
                    break;
                }
                else {
                    if (sd >= sq) {
                        sd -= sq;
                        printf("Saque efetuado com sucesso! Seu saldo é R$ %.2f\n", sd);
                        printf("\nPara voltar ao menu anterior, digite 9! \n");
                        break;
                    } else {
                        printf("Saldo insuficiente para sacar! Seu saldo é R$ %.2f\n", sd);
                        printf("\nPara voltar ao menu anterior, digite 9! \n");
                        break;
                    }

                }

            break;

            case '3':
                printf("Digite o Valor para depositar: R$ \n");
                if(scanf("%f", &dp) != 1){
                    break;
                }
                else {
                    sd += dp;
                    printf("Depósito efetuado com sucesso! Seu saldo é R$ %.2f\n", sd);
                    printf("\nPara voltar ao menu anterior, digite 9! \n");
                    break;
                }

            case '4':
                printf("Muito Obrigado por utilizar nossos serviços! Volte sempre.\n");
                return 0;

            case '9':
                return main();

            default:
                printf("Valor ou Opção invalida!\n\n");
                printf("\nPara voltar ao menu anterior, digite 9! \n");
                break;
        }

    }
    return 0;
}
