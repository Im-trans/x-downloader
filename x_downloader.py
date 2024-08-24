import argparse
import os
import sys
import validators

import yt_dlp

def baixar_video_twitter(url, pasta_download):
    try:
        ydl_opts = {
            'outtmpl': f'{pasta_download}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print(f"Download concluído! Vídeo salvo em: {pasta_download}")

    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='X Video Downloader CLI - Versão 1.0')

    parser.add_argument('-l', '--link-video', action='store', dest='link_url',required=True, help='URL/Link do video')
    parser.add_argument('-f', '--folder', action='store', dest='folder', required=False, help='Pasta onde o video será salvo')

    if len(sys.argv) == 0:
        parser.print_help()
        sys.exit(1)

    try:
        args = parser.parse_args()
    except Exception as err:
        parser.error(f'Ocorreu um erro dirante a passagem de argumentos: {err}')

    folder = '.'
    if args.folder:
        if not os.path.exists(args.folder):
            try:
                os.mkdir(args.folder)
            except PermissionError as err:
                err_msg = f'O usuário autenticado no sistema não tem permissão para criação de pastas!\n\n\t\tERROR: {err}'
                print(err_msg)
                sys.exit(1)
            except Exception as err:
                print(
                    f'An error occurred: {err} when creating folder {args.folder}! The program cannot continue...')
                sys.exit(1)
        folder = args.folder

    if not bool(args.link_url):
        parser.error("O link da url do vídeo é obrigatório!")

    if not validators.url(args.link_url):
        parser.error(f'A URL/Link fornecida \"{args.link_url}\" não parece ser válida! Por favor verifique...')

    url = args.link_url

    try:
        baixar_video_twitter(url, folder)
        print("\n\nO download do vídeo foi finalizado com sucesso!")
    except Exception as err:
        print(f"\n\nOcorreu um erro durante a tentativa de download: Error:{err}")
