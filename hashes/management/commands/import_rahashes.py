import re
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from hashes.models import RomHash

MD5_LINE_RE = re.compile(r'^([0-9a-fA-F]{32})\s+(.+)$')

class Command(BaseCommand):
    help = "Importa um arquivo de hashes (md5<TAB>nome) para RomHash"

    def add_arguments(self, parser):
        parser.add_argument("path", type=str)
        parser.add_argument("--source", default="")

    def handle(self, *args, **opts):
        path = Path(opts["path"])
        if not path.exists():
            raise CommandError(f"Arquivo não encontrado: {path}")

        created = skipped = invalid = 0

        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue

            match = MD5_LINE_RE.match(line)
            if not match:
                self.stderr.write(self.style.WARNING(
                    f"Linha inválida, ignorada: {line[:60]}"
                ))
                invalid += 1
                continue

            md5 = match.group(1).lower()
            file_name = match.group(2).strip()

            obj, was_created = RomHash.objects.get_or_create(
                md5=md5,
                defaults={
                    "file_name": file_name,
                    "source": opts["source"],
                },
            )
            if was_created:
                created += 1
            else:
                skipped += 1

        self.stdout.write(self.style.SUCCESS(
            f"Concluído: {created} criados, {skipped} já existiam, {invalid} inválidos."
        ))
