import { useState, useEffect } from 'react';
import { useWebSocket } from '../hooks/useWebSocket';

type Device = {
    address: string;
    name: string;
    type: string;
    rssi?: number;
};

export default function DeviceList() {
    const [devices, setDevices] = useState<Device[]>([]);
    
    const { send } = useWebSocket('ws://localhost:8000/ws/scan', {
        onMessage: (message) => {
            if (message.event === 'scan_results') {
                setDevices(message.data.results);
            }
        }
    });

    useEffect(() => {
        send({ event: 'start_scan', type: 'combined' });
    }, []);

    return (
        <div className="space-y-4">
            {devices.map((device) => (
                <div key={device.address} className="p-4 border rounded-lg hover:bg-gray-50">
                    <h3 className="font-medium">{device.name}</h3>
                    <p className="text-sm text-gray-500">{device.address}</p>
                    <div className="flex justify-between mt-2">
                        <span className="text-xs bg-blue-100 px-2 py-1 rounded">
                            {device.type}
                        </span>
                        {device.rssi && (
                            <span className="text-xs bg-green-100 px-2 py-1 rounded">
                                RSSI: {device.rssi} dBm
                            </span>
                        )}
                    </div>
                </div>
            ))}
        </div>
    );
}
