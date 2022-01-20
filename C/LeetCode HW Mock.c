typedef struct {
    int id[1001];
    int timeStamp[1001];
    int currentIdx;
} LogSystem;

LogSystem *LogSystemCreate()
{
    LogSystem *obj = (LogSystem* )malloc(sizeof(LogSystem) * 1);
    for (int i = 0; i < 1000; i++) {
        obj->id[i] = 0;
        obj->timeStamp[i] = 0;
    }
    obj->currentIdx = 0;
    return obj;
}

void LogSystemAdd(LogSystem *obj, int id, int timeStamp)
{
    obj->id[obj->currentIdx] = id;
    obj->timeStamp[obj->currentIdx] = timeStamp;
    (obj->currentIdx)++;
}

int LogSystemDelete(LogSystem *obj, int id)
{
    for (int i = 0; i <= obj->currentIdx; i++) {
        if (obj->id[i] == id) {
            obj->id[i] = -INT_MAX;
            obj->timeStamp[i] = -INT_MAX;
            return 0;
        }
    }
    return -1;
}

int LogSystemQuery(LogSystem *obj, int startTime, int endTime)
{   
    // In case user input a non-positive integer
    if (startTime <= 0) {
        startTime = 1;
    }
    int count = 0;
    for (int i = 0; i < obj->currentIdx; i++) {
        if (obj->timeStamp[i] >= startTime && obj->timeStamp[i] <= endTime) {
            count++;
        }
    }
    return count;
}

void LogSystemFree(LogSystem *obj)
{
    free(obj);
}
