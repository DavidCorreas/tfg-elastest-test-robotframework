import jenkins.*
import jenkins.model.*
import hudson.*
import hudson.model.*
import groovy.io.FileType


def clean_screenshots(){
    long startTime = System.currentTimeMillis()

    //Get value from String Parameter
    MAX_BUILDS = manager.build.buildVariables.get("MAX_BUILDS").toInteger()
    FOLDER = manager.build.buildVariables.get("FOLDER")

    for (job in Jenkins.instance.getAllItems(Job.class)) {
        manager.listener.logger.println "\n ***Job Name: ${job.name} ***" as java.lang.Object
        if (!job.url.contains(FOLDER)){
            manager.listener.logger.println "---> Skipped. Not in '${FOLDER}'" as java.lang.Object
            continue
        }

        SortedMap<Integer,List<File>> build_paths  = new TreeMap<Integer, List<File>>(new DescOrder())

        for(build in job.getBuilds()) {
            File folder = build.getRootDir()

            manager.listener.logger.println "----Build ID: ${build.id} -- Number: ${build.number}  -----" as java.lang.Object
            manager.listener.logger.println "----Build root dir: $folder ----" as java.lang.Object

            folder.listFiles().each {
                manager.listener.logger.println "Fichero: $it" as java.lang.Object

                if (build_paths.containsKey(build.number))
                    build_paths.get(build.number).add(it)
                else {
                    List<File> list = new ArrayList<File>()
                    list.add(it)
                    build_paths.put(build.number, list)
                }
            }
        }
            //Delete the folders based on the build number
        int count = 0
        for(Map.Entry<Integer, List<File>> entry : build_paths.entrySet()) {
            if(count >= MAX_BUILDS) {
                manager.listener.logger.println "En delete Job: " + job.name + " Build: " + entry.getKey()
                deletePngs(entry.getValue())
            }
            else {
                manager.listener.logger.println "Save - " + entry
            }
            count ++
        }
    }

    long endTime   = System.currentTimeMillis()
    long totalTime = (long) ((endTime - startTime) / 1000)

    manager.listener.logger.println "Total Run time in seconds : " + totalTime
}


//Function to delete the folder

void deletePngs(List<File> files){
    for(File file : files) {
        if (file.isDirectory())
            deletePngs(file.listFiles() as List<File>)
        if( ! file.isFile() && file.exists())
        {
            file.eachFile (FileType.FILES) { f ->
                if (f.name.contains('.png')) {
                    f.delete()
                    manager.listener.logger.println "Deleted - " + f.name
                }
            }
        }
    }
}

//For Descending order TreeMap
class DescOrder implements Comparator<Integer> {
    @Override
    int compare(Integer o1, Integer o2) {
        return o2.compareTo(o1)
    }
}

clean_screenshots()
