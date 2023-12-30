# @param {String} address
# @return {String}
def defang_i_paddr(address)
    defangedchars = address.chars
    index = 0
    while index < defangedchars.length
        if defangedchars[index] == "."
            defangedchars.insert((index + 1), "]")
            defangedchars.insert(index, "[")
            index += 2
        else
            index += 1
        end       
    end
    defanged = defangedchars.join
    return defanged
end