from totalsegmentator import libs
from multiprocessing import Pool
from progress.bar import Bar
from tqdm import tqdm

def job(task_id):
    libs.download_pretrained_weights(task_id=task_id)
    print(f"weights downloaded for task: {task_id}")


def download_parallel(tasks):
    pool = Pool()
    bar = Bar('Processing', max=len(tasks))
    for i in pool.imap(job, tasks):
        bar.next()
    bar.finish()


def download_sequential(tasks):
    for task_id in tqdm(tasks):
        job(task_id)


if __name__ == '__main__':
    tasks = [251, 252, 253, 254, 255, 256]

    # download_parallel(tasks)
    download_sequential(tasks)
