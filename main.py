import sys
import time


def generatepage(temp_lines, temp, counter):

    f = open("menu"+str(counter)+".asset", "x")
    f.write("%YAML 1.1\n" +
            "%TAG !u! tag:unity3d.com,2011:\n" +
            "--- !u!114 &11400000\n" +
            "MonoBehaviour:\n" +
            "  m_ObjectHideFlags: 0\n" +
            "  m_CorrespondingSourceObject: {fileID: 0}\n" +
            "  m_PrefabInstance: {fileID: 0}\n" +
            "  m_PrefabAsset: {fileID: 0}\n" +
            "  m_GameObject: {fileID: 0}\n" +
            "  m_Enabled: 1\n" +
            "  m_EditorHideFlags: 0\n" +
            "  m_Script: {fileID: -340790334, guid: 67cc4cb7839cd3741b63733d5adf0442, type: 3}\n" +
            "  m_Name: menu"+str(counter)+"\n" +
            "  m_EditorClassIdentifier: \n" +
            "  controls:\n")
    i = 0
    while i <= 8:
        if temp >= 0:
            tmp_line = str(temp_lines[temp])
            # tmp_line = re.sub('\w','',tmp_line)
            f.write("  - name: " + str(tmp_line) + "\n" +
                    "    icon: {fileID: 2800000, guid: 814c40cdd23a7fe488c8826cf7d9b315, type: 3}\n" +
                    "    type: 103\n" +
                    "    parameter:\n" +
                    "      name: \n" +
                    "    value: 1\n" +
                    "    style: 0\n" +
                    "    subMenu: FIXMEDRISCOLL\n" +
                    "    subParameters: []\n" +
                    "    labels: []\n")
            temp -= 1
        i += 1
    f.close()
    return temp


startTime = time.time()
if len(sys.argv) <= 1:
    print('Avatars 3.0 TEXT TO SUBMENU Python Help:')
    print('Usage: text2submenu.py (pre/post) (link-to-plaintext/link-to-folder) [biggest]')
    print("Run pre in a folder OUTSIDE of your unity project. Then, run post INSIDE your unity project INSIDE the folder. (READ MY DOCUMENTATION)")
    print("TXT file must be in plaintext, UTF8!")
else:
    if sys.argv[1] == "pre":
        print('Processing ' + str({sys.argv[2]}) + '... Please wait!')
        with open(sys.argv[2]) as f:
            temp_lines = f.readlines()
            temp_lines = [x.strip() for x in temp_lines]
            temp = len(temp_lines)-1

            counter = 0
            while temp > 0:
                temp = generatepage(temp_lines, temp, counter)
                temp -= 1
                counter += 1
    else:
        if sys.argv[1] == "post":
            print("Processing folder.. please wait!")
            oldFolder = int(sys.argv[3])
            while oldFolder >= 0:
                asset = open("menu" + str(oldFolder) + ".asset")
                meta = open("menu" + str(oldFolder) + ".asset.meta")
                lines = meta.readlines()
                guid = lines[1].replace("guid: ", "")
                meta.close()
                lines = asset.readlines()
                i = 0
                while i < len(lines):
                    lines[i] = lines[i].replace("FIXMEDRISCOLL", "{fileID: 11400000, guid: "+str(guid)+", type: 2}")
                    i += 1
                overwriteasset = open("menu" + str(oldFolder) + ".asset", "w")
                overwriteasset.writelines(lines)
                overwriteasset.close()
                asset.close()
                oldFolder -= 1
    print('Job completed, took', time.time() - startTime, 's to run.');