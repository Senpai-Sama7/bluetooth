import { useEffect, useState } from "react"
import useApi from "../hooks/useApi"
import DeviceList from "../components/DeviceList"

export default function Dashboard() {
  const [devices, setDevices] = useState([])

  useEffect(() => {
    useApi.post('/scan/all', { interface: 'hci0', duration: 10 })
      .then(res => setDevices(res.devices))
  }, [])

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">Device Dashboard</h1>
      <DeviceList devices={devices} />
    </div>
  )
}
