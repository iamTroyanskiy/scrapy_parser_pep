import collections
from datetime import datetime

from pep_parse.settings import BASE_DIR, DATETIME_PATTERN
from pep_parse.utils import dict_to_csv


class PepParsePipeline:
    def open_spider(self, spider):
        self.total_statuses = collections.defaultdict(int)

    def process_item(self, item, spider):
        status = item['status']
        self.total_statuses[status] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        now = datetime.now().strftime(DATETIME_PATTERN)
        filename = f'status_summary_{now}.csv'
        file_path = results_dir / filename
        head = ('Статус', 'Количество')
        dict_to_csv(
            file_path,
            self.total_statuses,
            head
        )
